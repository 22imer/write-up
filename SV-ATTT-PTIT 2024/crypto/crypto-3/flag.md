Do ta có 2 message trong output.txt:
THIS IS A FORM FLAG: PTITCTF{This_is_a_fake_flag}
flag
được mã hoá bằng aes ctr có cơ chế giống xor:
ta xor mess đã biết với mess mã hoá => key_xor
rồi giải mã: key_xor ^ encrypted_mess => flag

flag: PTITCTF{Now_You_Know_AES_So_Ez}
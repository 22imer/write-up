Ta tìm mật khẩu file rar bằng hashcat
mk: 123456789d
mở hxd check lại magic byte thì ta thấy các cặp bit bị đổi cho nhau
Dùng solve.py ta tìm ra được bức ảnh
theo link https://github.com/H4lst0n/naunau/blob/main/README.md
dùng cyberchef ta giải được mã base64 và base32 lồng nhau
flag: PTITCTF{T0n_T0n_1s_My_Fr13nd!@#txc!@#}
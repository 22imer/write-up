Đọc hxd của file chall.jpg ta thấy được mã magic byte của file pe bị đảo ngược ở cuối file\
đảo được file thì t có được một file pe 
t thấy ở func_d có print flag
lướt qua các func_ a,b,c,d,e
ta thấy được func_a gọi func_c
trong func_c ta thấy được:
function_b(a50eD8, 14, byte_6E94302A);
function_d(&unk_6E943020, 39, a50eD8);
ta có a50eD8 = "<5=:0e:',7,':d&8`,"

Trong func_b ta thấy là 1 function xor(địa chỉ value_xor,len_value,key_xor)
key xor là bit đầu của byte_6E94302A ta thấy func_b lấy char của byte = 1 bit
func_b(a50eD8,14,54h)
sau khi xor xong a50eD8 = haind1nSn0rl4x

function_d(&unk_6E943020, 39, a50eD8);
Từ ảnh data.png ta thấy 39 bit của &unk_6E943020 là 
0x70, 0x0AE, 0x8A, 0x4D , 0x8C, 0x73 , 0x15, 0x5A , 0x0EC, 0x0CC, 0x54 , 0x28 , 0x32 , 0x45 , 0x0F0, 0x39 , 0x27 , 0x25 , 0x0E6, 4, 0x6A , 0x38 , 0x4F , 0x0F9, 0x5B , 0x95, 0x24 , 0x9D, 0x9D, 0x0D1, 0x9C, 0x37 , 0x0E9, 0x0AB, 0x98, 0x0A4, 0x0A4, 0x7B , 0x0C1
có function_e(a50eD8,14,&unk_6E943020, 39)
ta biết được func_e là mã hoá rc4
sau khi function_d chạy thì 
unk_ sẽ được mã hoá rc4 với key haind1nSn0rl4x
ra được flag
viết script python mã hoá rc4 ta có được

flag :PTITCTF{D11_In_Front_Of_IMG_6861696e64}
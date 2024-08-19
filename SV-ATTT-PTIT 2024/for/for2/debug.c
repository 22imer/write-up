int __fastcall main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // rax
  char Buffer[112]; // [rsp+20h] [rbp-60h] BYREF
  int v6[34]; // [rsp+90h] [rbp+10h]
  int v7; // [rsp+118h] [rbp+98h]
  int i; // [rsp+11Ch] [rbp+9Ch]

  _main();
  v6[0] = 53;
  v6[1] = 57;
  v6[2] = 46;
  v6[3] = 57;
  v6[4] = 40;
  v6[5] = 57;
  v6[6] = 43;
  v6[7] = 96;
  v6[8] = 24;
  v6[9] = 93;
  v6[10] = 85;
  v6[11] = 21;
  v6[12] = 87;
  v6[13] = 89;
  v6[14] = 68;
  v6[15] = 43;
  v6[16] = 22;
  v6[17] = 81;
  v6[18] = 24;
  v6[19] = 68;
  v6[20] = 43;
  v6[21] = 87;
  v6[22] = 21;
  v6[23] = 82;
  v6[24] = 68;
  v6[25] = 85;
  v6[26] = 72;
  v6[27] = 25;
  v6[28] = 85;
  v6[29] = 9;
  v6[30] = 98;
  v7 = 31;
  printf("Nhap vao mot chuoi: ");
  v3 = __iob_func();
  fgets(Buffer, 100, v3);
  Buffer[strcspn(Buffer, "\n")] = 0;
  if ( strlen(Buffer) == v7 )
  {
    for ( i = 0; i < v7; ++i )
    {
      if ( Buffer[i] - 27 != v6[i] )
        goto LABEL_2;
    }
    puts("Correct!");
    return 0;
  }
  else
  {
LABEL_2:
    puts("Wrong!");
    return 0;
  }
}
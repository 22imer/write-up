int sub_401530()
{
  int v1; // [rsp+28h] [rbp-8h]
  int i; // [rsp+2Ch] [rbp-4h]

  printf("This is your flag: ");
  v1 = strlen(Str);
  for ( i = 0; i <= 25; ++i )
    printf("%d ", dword_403040[i] ^ (unsigned int)Str[i % v1]);
  return putchar(10);
}
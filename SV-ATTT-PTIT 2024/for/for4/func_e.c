__int64 __fastcall function_e(__int64 a1, int a2, _BYTE *a3, int a4)
{
  __int64 i; // r10
  __int64 result; // rax
  __int64 v6; // rdx
  char v7; // r10
  char v8; // si
  __int64 v9; // rcx
  __int64 v10; // rdx
  _BYTE *v11; // rsi
  char v12; // al
  char v13; // bl
  char v14[536]; // [rsp+0h] [rbp-218h]

  for ( i = 0LL; i != 256; ++i )
  {
    v14[i] = i;
    v14[i + 256] = *(_BYTE *)(a1 + (int)i % a2);
  }
  result = 0LL;
  LOBYTE(v6) = 0;
  do
  {
    v7 = v14[result];
    v8 = v14[(unsigned __int8)(v14[result + 256] + v7 + v6)];
    v6 = (unsigned __int8)(v14[result + 256] + v7 + v6);
    v14[result++] = v8;
    v14[v6] = v7;
  }
  while ( result != 256 );
  if ( a4 > 0 )
  {
    LOBYTE(v9) = 0;
    LOBYTE(v10) = 0;
    v11 = &a3[a4 - 1 + 1];
    do
    {
      v12 = v14[(unsigned __int8)(v10 + 1)];
      v10 = (unsigned __int8)(v10 + 1);
      v13 = v14[(unsigned __int8)(v12 + v9)];
      v9 = (unsigned __int8)(v12 + v9);
      v14[v10] = v13;
      v14[v9] = v12;
      result = (unsigned __int8)v14[(unsigned __int8)(v14[v10] + v12)];
      *a3++ ^= result;
    }
    while ( a3 != v11 );
  }
  return result;
}
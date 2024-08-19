int __fastcall function_d(void *Src, int a2, const char *a3)
{
  HANDLE CurrentProcess; // rax
  void *v7; // rsi
  unsigned int v8; // eax
  const char *v9; // rax
  __int64 i; // r10
  BOOL pbDebuggerPresent; // [rsp+2Ch] [rbp-2Ch] BYREF

  CurrentProcess = GetCurrentProcess();
  if ( CheckRemoteDebuggerPresent(CurrentProcess, &pbDebuggerPresent) && pbDebuggerPresent )
    ExitProcess(0xFFFFFFFF);
  v7 = malloc(a2);
  memcpy(v7, Src, a2);
  v8 = strlen(a3);
  function_e(a3, v8, v7, (unsigned int)a2);
  printf("Your Flag: ");
  v9 = (const char *)malloc(a2 + 1);
  if ( !v9 )
    exit(1);
  for ( i = 0LL; a2 > (int)i; ++i )
    v9[i] = *((_BYTE *)v7 + i);
  v9[a2] = 0;
  return printf("%s", v9);
}
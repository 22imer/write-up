void __fastcall function_b(_BYTE *a1, int a2, char a3)
{
  _BYTE *v4; // rbx
  _BYTE *v5; // r13
  HANDLE CurrentProcess; // rax
  BOOL pbDebuggerPresent; // [rsp+2Ch] [rbp-3Ch] BYREF

  if ( a2 > 0 )
  {
    v4 = a1;
    v5 = &a1[a2 - 1 + 1];
    do
    {
      CurrentProcess = GetCurrentProcess();
      if ( CheckRemoteDebuggerPresent(CurrentProcess, &pbDebuggerPresent) && pbDebuggerPresent )
        ExitProcess(0xFFFFFFFF);
      *v4++ ^= a3;
    }
    while ( v4 != v5 );
  }
}
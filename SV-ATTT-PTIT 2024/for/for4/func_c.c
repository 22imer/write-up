int function_c()
{
  HANDLE CurrentProcess; // rax
  BOOL pbDebuggerPresent; // [rsp+2Ch] [rbp-Ch] BYREF

  CurrentProcess = GetCurrentProcess();
  if ( !CheckRemoteDebuggerPresent(CurrentProcess, &pbDebuggerPresent) || !pbDebuggerPresent )
    return printf("DebugPlease");
  function_b(a50eD8, 14, byte_6E94302A);
  return function_d(&unk_6E943020, 39, a50eD8);
}
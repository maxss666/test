.globl check_of

check_of:
    movb $100, %r10b
    movb $28, %r9b
    addb %r9b, %r10b
    jo .l1
    jmp .l2
.l1:
    movq $1, %rax
    ret 
.l2:
    movq $0, %rax
    ret 

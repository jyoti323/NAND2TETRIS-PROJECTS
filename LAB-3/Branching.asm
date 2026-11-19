// B) Checks if RAM[0] > 0. Sets RAM[1] = 1 if true, else 0.

@0          
D=M        
@POSITIVE   
D;JGT       


@1          
M=0         
@END        
0;JMP      


(POSITIVE)
@1          
M=1         


(END)
@END
0;JMP


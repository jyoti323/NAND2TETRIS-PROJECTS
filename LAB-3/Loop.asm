// C) Counts up to 5 using a loop and stores the final result in RAM[2]


@5          
D=A         
@0         
M=D        

@1         
M=0          


(LOOP)
@0          
D=M          
D;JLE      

@1         
M=M+1      

@0          
M=M-1      

@LOOP       
0;JMP       


(END)
@1         
D=M         
@2          
M=D        


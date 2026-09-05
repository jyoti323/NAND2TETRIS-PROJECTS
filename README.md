# NAND2TETRIS-PROJECTS
IT  Include the projects of My course Nand2Tetris

ZOSIMA QUESTIONS:

Q-1: Implement NOT, AND, OR gates
SOL:
CHIP And {
    IN a, b;
    OUT out;
    
    PARTS:
    Nand(a=a , b=b,out= nandOut );
    Not(in=nandOut , out=out);
    
}

CHIP Or {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a , b=a , out=anandOut );
    Nand(a=b , b=b , out=bnandOut );
    Nand(a= anandOut, b=bnandOut , out=out );
   
}

CHIP Not {
    IN in;
    OUT out;

    PARTS:
    Nand(a=in , b=in , out=out );
    
}

Q-2: Implement XOR, Mux (2-way, 4-way), and DMux chips in HDL.

CHIP Xor {
    IN a, b;
    OUT out;

    PARTS:
    Nand(a=a, b= b, out= anandOut );
    Nand(a=a , b=anandOut , out=bnandOut );
    Nand(a=b , b=anandOut, out=cnandOut );
    Nand(a=bnandOut , b=cnandOut , out=out );

}

CHIP Mux {
    IN a, b, sel;
    OUT out;

    PARTS:
    Not(in=sel,out=notSel);
    And(a=a , b=notSel , out=w1 );
    And(a=b, b=sel , out=w2 );
    Or(a=w1 , b= w2, out=out );
    
}

CHIP Mux4Way16 {
    IN a[16], b[16], c[16], d[16], sel[2];
    OUT out[16];
    
    PARTS:
    Mux16(a=a , b=b , sel=sel[0] , out=w1 );
    Mux16(a=c , b=d , sel=sel[0] , out=w2 );
    Mux16(a=w1 , b=w2 , sel=sel[1] , out=out );
    
}

CHIP DMux {
    IN in, sel;
    OUT a, b;

    PARTS:
    Not(in= sel , out= nsel);
    And(a= in , b= nsel , out=a );
    And(a= in , b=sel , out=b );

}

Q-3: Build the Half Adder and Full Adder chips in HDL.
CHIP FullAdder {
    IN a, b, c;   
    OUT sum,     
        carry;   

    PARTS:

    HalfAdder (a=a, b=b,sum=S1, carry=C1);
    HalfAdder (a=S1, b=cin,sum=sum, carry=C2);

    Or( a=C1, b=C2, out= carry);

}

CHIP HalfAdder {
    IN a, b, c;   
    OUT sum,     
        carry;   

    PARTS:

    Xor(a=a, b=b,out=sum);
    And (a=a, b=b,out=carry);

}
    








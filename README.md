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





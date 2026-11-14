Part A– Build the computer  

Join your lab chips (gates, ALU, registers, RAM, PC) into CPU.hdl, Memory.hdl and Computer.hdl.

Check them with the official test files (CPU.tst, Memory.tst, ComputerAdd.tst, ComputerMax.tst, ComputerRect.tst) and take a screenshot of each result. If one of your older chips does not work, you may use the built-in chip, but mention it in your report.

<img width="1365" height="658" alt="computer1" src="https://github.com/user-attachments/assets/f5b906e7-4cde-4bcd-891f-3d383369dd28" />
<img width="1366" height="650" alt="memory1" src="https://github.com/user-attachments/assets/c90ad54d-e5f1-4832-873a-aff843200da9" />
<img width="1366" height="651" alt="cpu1" src="https://github.com/user-attachments/assets/cea1600a-5ca6-47b0-a229-a68caa57f051" />



Part B:-
Write a small assembler in Python The assembler turns a Hack program (.asm) into 0s and 1s (.hack). 
First reading: remove comments and blank lines, and note where each label like (LOOP) is. 
Second reading: turn every line into 16 bits. New variables get RAM addresses 16, 17, 18 and so on. Test on Add.asm, Max.asm, Rect.asm and Pong.asm. 

The output must match the official assembler.
<img width="1366" height="628" alt="WhatsApp Image 2026-11-14 at 9 56 54 AM" src="https://github.com/user-attachments/assets/89630bf1-3f71-4c47-b643-0d54121f049f" />
<img width="1366" height="639" alt="WhatsApp Image 2026-11-14 at 9 58 15 AM" src="https://github.com/user-attachments/assets/024faf0d-e1c6-456a-bb7c-83dc93d74246" />
<img width="1366" height="639" alt="WhatsApp Image 2026-11-14 at 9 37 33 AM" src="https://github.com/user-attachments/assets/19a8050d-ea88-483e-b9dd-c83ce579b257" />
<img width="1366" height="643" alt="WhatsApp Image 2026-11-14 at 9 35 13 AM" src="https://github.com/user-attachments/assets/56a34a8b-89ea-4e8a-b4c2-dbcf0fd8bcb9" />

One extra feature, based on K: K mod 3 Extra feature 0 Save all labels and variables with their addresses in symbols.txt. 1 2 For a wrong line, print a clear message with the line number (e.g. Line 7: invalid instruction) instead of crashing. Print a warning if the same label is written twice.
<img width="1366" height="707" alt="WhatsApp Image 2026-11-14 at 9 49 00 AM" src="https://github.com/user-attachments/assets/5e275175-d921-4af9-acec-4a693ddb2cac" />


PART C :- 
Write Box.asm in Hack assembly. While any key is pressed, a black box appears. When the key is released, the box disappears. ˆ ˆ 
Your box: starts at row K, is 20 rows tall, and is 16 ×((K mod 4)+1) pixels wide from the left edge. 
Convert it with your own assembler from Part B (not the official one), run it in the CPU Emulator, and take a screenshot of your box.

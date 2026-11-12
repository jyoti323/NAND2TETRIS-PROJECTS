Part A– Build the computer  

Join your lab chips (gates, ALU, registers, RAM, PC) into CPU.hdl, Memory.hdl and Computer.hdl.

Check them with the official test files (CPU.tst, Memory.tst, ComputerAdd.tst, ComputerMax.tst, ComputerRect.tst) and take a screenshot of each result. If one of your older chips does not work, you may use the built-in chip, but mention it in your report.

<img width="1365" height="658" alt="Compter" src="https://github.com/user-attachments/assets/28d3ce92-ee62-44f7-8eb7-efa4654900e4" />
<img width="1366" height="642" alt="Memory" src="https://github.com/user-attachments/assets/da3a8406-7113-454b-b8d3-c71f610cf1b9" />
<img width="1366" height="618" alt="CPU" src="https://github.com/user-attachments/assets/23bbed7f-bae5-477b-ac4d-ea99513b8fb2" />


Part B– Write a small assembler in Python The assembler turns a Hack program (.asm) into 0s and 1s (.hack). ˆ ˆ ˆ ˆ 
First reading: remove comments and blank lines, and note where each label like (LOOP) is. 
Second reading: turn every line into 16 bits. New variables get RAM addresses 16, 17, 18 and so on. Test on Add.asm, Max.asm, Rect.asm and Pong.asm. 
The output must match the official assembler. 
One extra feature, based on K: K mod 3 Extra feature 0 Save all labels and variables with their addresses in symbols.txt. 1 2 For a wrong line, print a clear message with the line number (e.g. Line 7: invalid instruction) instead of crashing. Print a warning if the same label is written twice.

Write Box.asm in Hack assembly. While any key is pressed, a black box appears. When the key is released, the box disappears. ˆ ˆ 
Your box: starts at row K, is 20 rows tall, and is 16 ×((K mod 4)+1) pixels wide from the left edge. 
Convert it with your own assembler from Part B (not the official one), run it in the CPU Emulator, and take a screenshot of your box.

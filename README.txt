
# µVision ARM assembly formatter
# Made by Eric Eaton 9/25/2023 for educational use.
# This is extremely helpful to interactively understand how compilers convert c code into assembly.

# Boilerplate: This is free to use and distribute. I am not liable for anything that people do with it. It has no guarentee of working.

# This will convert copied assembly from µVision's Debugger's Disassembly to ARM assembly that can be copied and pasted in a function
# This works for both mixed mode and assembly mode
# It has been tested on a few functions, but not extensively

# To use it:
# 1. In µVision, execute code in the debugger and open the Disassembly to see the assembly code.
# 2. copy and paste one function of assembly code from the Disassembly into a new text file
# 4. run this script and follow the prompts. A text file will be created with the same name as your original file but appended with the suffix "-ARMFormatted".

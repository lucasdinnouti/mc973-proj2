for FILE in ./test/*
do
	riscv64-unknown-elf-objcopy -O binary -j .text -j .rodata $FILE $FILE.bin
done
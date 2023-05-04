# RISC-V - SIMULATOR

## Requirements

Before running the simulator, make sure you have these dependencies installed.

* Python3
* riscv64-linux-gnu-objcopy

## Programs

Considering compiled programs in elf format.

Reference: https://drive.google.com/drive/u/1/folders/1ei8E-qk2dwQvCWJv8ovGJiIdLjw7yVfP

## Running for all test programs

To make it easier, you can run the simulator for all programs in a folder.

```
./run.sh <FOLDER>
```

For example:

```
./run.sh ./test
```

The output log files will be saved in the ./test folder.

## Running for a single program

### Convert program files to .bin

The simulator expects to read binary files. To convert the given elf file, please run the conversion script:

```
./convert.sh
```

This script uses objcopy.

### Execution

For getting the program execution logs, just run:

```
python3 main.py tests/<PROGRAM>
```

For example:

```
python3 main.py tests/000.main.riscv.bin
```

This will generate a log file on the `./test` folder.
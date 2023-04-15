all: test


test: test.c dockcross-x86
	./dockcross-x86 bash -c 'sudo $$CXX test2.c -O0  -m64 -Xlinker -Map=output.map -o test -static'

dockcross-x86:
	docker run --rm dockcross/linux-x86 > ./dockcross-x86
	chmod +x ./dockcross-x86

clean:
	rm -f dockcross-x86 test

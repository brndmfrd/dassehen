setup : setup.py 
	python setup.py build
	python setup.py install

test : 
	./dassehen/tests/runAllTests.sh

clean :
	rm *~

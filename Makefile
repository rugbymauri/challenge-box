install:
	pip install pygame


start:
	python main.py

sync:
	rsync -r . admin@cqc.local:/home/admin/game

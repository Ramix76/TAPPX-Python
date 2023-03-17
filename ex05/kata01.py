kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
it = kata.items()

__name__ == "__main__"
for x, y in list(it):
    print(x, "was created by", y)

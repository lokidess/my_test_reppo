a = ["wer", "qw", "werd", "werdfssfd", "sdf", "ase"]
print(f"Origin: {a}")
b = sorted(a, key=lambda x: len(x), reverse=True)
a[a.index(b[0])], a[a.index(b[-1])] = a[a.index(b[-1])], a[a.index(b[0])]
print(f"Replaced: {a}")



from random import randint

class Generator:
  def generate(self, count):
    return [randint(1,9) for x in range(count)]

class Splitter:
  def split(self, array):
    result = []

    row_count = len(array)
    col_count = len(array[0])

    for r in range(row_count):
      the_row = []
      for c in range(col_count):
        the_row.append(array[r][c])
      result.append(the_row)

    for c in range(col_count):
      the_col = []
      for r in range(row_count):
        the_col.append(array[r][c])
      result.append(the_col)

    diag1 = []
    diag2 = []

    for c in range(col_count):
      for r in range(row_count):
        if c == r:
          diag1.append(array[r][c])
        r2 = row_count - r - 1
        if c == r2:
          diag2.append(array[r][c])

    result.append(diag1)
    result.append(diag2)

    return result

class Verifier:
  def verify(self, arrays):
    first = sum(arrays[0])

    for i in range(1, len(arrays)):
      if sum(arrays[i]) != first:
        return False

    return True

class MagicSquareGenerator:
  def generate(self, size):
    # todo - return a magic square of the given size
    g = Generator()
    v = Verifier()
    s = Splitter()

    while True:
      gen_array = []
      for _ in range(size):
        gen_array.append(g.generate(size))
      split_array = s.split(gen_array)
      verify_result = v.verify(split_array)
      if verify_result:
        break
    return gen_array
      

def main():
    count = 2
    msg = MagicSquareGenerator()
    magic_square = msg.generate(count)

    print(magic_square)

main()
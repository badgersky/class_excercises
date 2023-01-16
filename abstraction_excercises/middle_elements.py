def middle_elements(iterators):
    return [iterator[int(len(iterator) / 2)] for iterator in iterators if iterator]


class SequenceOfNumbers:

    def __init__(self, start, stop, step):
        self.step = step
        self.stop = stop
        self.start = start

    def __len__(self):
        return (self.stop - self.start) // self.step

    def __getitem__(self, item):
        if item < 0:
            raise IndexError(f'Wrong Index: {item}')
        if self.start + self.step * item >= self.stop:
            raise IndexError(f'Wrong index: {item}')
        return self.start + self.step * item



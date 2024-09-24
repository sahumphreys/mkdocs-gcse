import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    frequency_map = defaultdict(int)

    for char in data:
        frequency_map[char] += 1

    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(None, left.frequency + right.frequency)
        merged_node.left = left
        merged_node.right = right

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(node, current_code="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = {}

    if node is not None:
        if node.char is not None:
            huffman_codes[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", huffman_codes)
        build_huffman_codes(node.right, current_code + "1", huffman_codes)

def view_frequency_table(data):
    frequency_map = defaultdict(int)

    for char in data:
        frequency_map[char] += 1

    print("Frequency Table:")
    for char, freq in frequency_map.items():
        print(f"{char}: {freq}")

def view_huffman_codes(huffman_codes):
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

def huffman_encode(data):
    root = build_huffman_tree(data)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    encoded_data = "".join(huffman_codes[char] for char in data)

    return encoded_data, root, huffman_codes

def huffman_decode(encoded_data, root):
    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data

def main():
    data = "hello world"

    view_frequency_table(data)

    encoded_data, huffman_tree, huffman_codes = huffman_encode(data)

    print("\nOriginal data:", data)
    print("Encoded data:", encoded_data)

    view_huffman_codes(huffman_codes)

    decoded_data = huffman_decode(encoded_data, huffman_tree)
    print("\nDecoded data:", decoded_data)

if __name__ == "__main__":
    main()

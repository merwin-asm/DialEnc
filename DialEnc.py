"""
DialEnc 1.0.0
An encryption  based on phone dialing system...
Author : Merwin
"""

class DialEnc:
    def __init__(self):
        pass
    def make_chunks_de(self,data):
        data += "00"
        chunks = []
        chunk = ""
        c = 0
        for e in data:
            if c % 2 == 0 and c != 0:
                chunks.append(chunk)
                chunk = ""
                c = 0
            chunk += e
            c += 1
        return chunks
    def convert_form_chunks(self,chunks):
        data  = ""
        letters = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"],
                   ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        for e in chunks:
            n_1 = int(e[0])
            n_2 = int(e[1])
            data+=letters[n_1][n_2]
        return data
    def get_char_id(self,letter):
        letters = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"],
                   ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        for e in range(0,9):
            try:
                index = letters[e].index(letter)
                return e,index
            except ValueError:
                pass
    """
    Encrypt your data...
    Parm Data:Str
    """
    def encrypt(self,data):
        data_enc = ""
        if data.isalpha():
            for e in data:
                n_1,n_2 = self.get_char_id(e)
                data_enc+= f"{n_1}{n_2}"
            return data_enc
        else:
            return False
    """
    Decrypt your data...
    Parm Data:Str
    """
    def decrypt(self,data):
        if data.isnumeric():
            chunks = self.make_chunks_de(data)
            data = self.convert_form_chunks(chunks)
            return data
        else:
            return False


if __name__ == '__main__':
    dialenc = DialEnc()
    enc_data = dialenc.encrypt("hello")
    print(f"Encrypted :  {enc_data}")
    dec_data = dialenc.decrypt(enc_data)
    print(f"Decrypted :  {dec_data}")

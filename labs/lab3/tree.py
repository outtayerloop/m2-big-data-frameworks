class Tree(object):

    def __init__(self, line):
        self.fields = line.split(';')

    def __str__(self):
        return 'Tree[%s]' % ', '.join(self.fields)

    def get_height(self):
        if self.fields[6] is not None and self.fields[6] != '':
            return float(self.fields[6])
        else:
            return None
        
    def get_kind(self):
        if self.fields[3] is not None and self.fields[3] != '':
            return self.fields[3]
        else:
            return None
        
    def get_name(self):
        if self.fields[9] is not None and self.fields[9] != '':
            return self.fields[9]
        else:
            return None
        
    def get_year(self):
        if self.fields[5] is not None and self.fields[5] != '':
            return int(self.fields[5])
        else:
            return None
        
    def get_district(self):
        if self.fields[1] is not None and self.fields[1] != '':
            return self.fields[1]
        else:
            return None
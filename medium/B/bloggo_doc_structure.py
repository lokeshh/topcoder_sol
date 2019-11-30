class bloggoDocStructure:
  def extract_child(self, raw_children):
    tag_name = ''
    start = False
    stop = False
    for i in range(len(raw_children)):
      if stop:
        break
      if raw_children[i] == '<':
        start = True
      elif raw_children[i] == '>':
        stop = True
      elif start:
        tag_name += raw_children[i]
    
    level = 0
    for j in range(i, len(raw_children) - 1):
      if raw_children[j] == '<' and raw_children[j:j+2] != '</':
        level += 1
      if raw_children[j:j+2] == '</':
        # breakpoint()
        if level == 0:
          return (
            self.build_node(tag_name, raw_children[i:j]),
            raw_children[j + len(tag_name) + 3:]
          )
        else:
          level -= 1

  def get_children_nodes(self, raw_children):
    children = []
    while raw_children != '':
      child, raw_children = self.extract_child(raw_children)
      children.append(child)
    return children

  def build_node(self, name, raw_children):
    n = Node(name, [])
    n.children = self.get_children_nodes(raw_children)
    return n

  def convert_to_tree(self, doc):
    doc = ''.join(doc)
    new_doc = ''
    tag_start = False
    for i in doc:
      if i == '<':
        new_doc += i
        tag_start = True
      elif i == '>':
        new_doc += i
        tag_start = False
      elif tag_start:
        new_doc += i

    tag_tree = self.extract_child(new_doc)[0]
    return tag_tree
    
  def in_tree(self, doc_a, doc_b):
    if doc_a.name != doc_b.name or len(doc_a.children) > len(doc_b.children):
      return False
    b_children_copy = doc_b.children[:]
    for child_a in doc_a.children:
      for idx, child_b in enumerate(b_children_copy):
        if self.in_tree(child_a, child_b):
          b_children_copy = b_children_copy[idx+1:]
          break
      else:
        return False
    return True

  def count_nodes(self, node):
    c = 1
    for child in node.children:
      c += self.count_nodes(child)
    return c

  def compare(self, doc_a, doc_b):
    doc_a = self.convert_to_tree(doc_a)
    doc_b = self.convert_to_tree(doc_b)
    doc_a_node_count = self.count_nodes(doc_a)
    doc_b_node_count = self.count_nodes(doc_b)
    if self.in_tree(doc_a, doc_b):
      if self.in_tree(doc_b, doc_a):
        return 'equivalent'
      else:
        return 'intree ' + str(doc_b_node_count - doc_a_node_count)
    elif self.in_tree(doc_b, doc_a):
      return 'outtree ' + str(doc_a_node_count - doc_b_node_count)
    else:
      return 'incompatible'

class Node:
  def __init__(self, name, children):
    self.name = name
    self.children = children
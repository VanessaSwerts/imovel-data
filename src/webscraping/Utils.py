import itertools

def getElementXPath(element):
  components = []
  child = element if element.name else element.parent
  for parent in child.parents:
      previous = itertools.islice(parent.children, 0, parent.contents.index(child))
      xpath_tag = child.name
      xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
      components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
      child = parent
  components.reverse()
  return '/%s' % '/'.join(components)
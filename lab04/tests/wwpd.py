test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab04 import *
          >>> t = tree(1, tree(2))
          8dfecce35cfbb620490b1aa9637bdafd
          # locked
          >>> t = tree(1, [tree(2)])
          5c5b429063049b010ee9d6da4aff0f09
          # locked
          >>> label(t)
          91b35c416e4c4ef4138ebfcce69874af
          # locked
          >>> label(branches(t)[0])
          61b793952531daad90d65377b695da99
          # locked
          >>> x = branches(t)
          >>> len(x)
          91b35c416e4c4ef4138ebfcce69874af
          # locked
          >>> is_leaf(x[0])
          46d1f016b6482a76a74835354edaab71
          # locked
          >>> branch = x[0]
          >>> label(t) + label(branch)
          62cb7be5b3f27b8761401e9f99897a30
          # locked
          >>> len(branches(branch))
          c4baa133341c5988be93c04ac3d055bb
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> from lab04 import *
          >>> b1 = tree(5, [tree(6), tree(7)])
          >>> b2 = tree(8, [tree(9, [tree(10)])])
          >>> t = tree(11, [b1, b2])
          >>> for b in branches(t):
          ...     print(label(b))
          05ddbbaaec055d602188518c1a14dc43
          a78f9116f634421eb2a6b7d7c5fc74dd
          # locked
          >>> for b in branches(t):
          ...     print(is_leaf(branches(b)[0]))
          46d1f016b6482a76a74835354edaab71
          61e74011ca20035e5cb51b814087a093
          # locked
          >>> [label(b) + 100 for b in branches(t)]
          bbe2a60fae62d1dcc643c07fefb2cb2f
          # locked
          >>> [label(b) * label(branches(b)[0]) for b in branches(t)]
          14abfd64a0e8741901fc2f6a3bab73d2
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}

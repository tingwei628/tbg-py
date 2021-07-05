def get_total_blocks():
    _block_1 = [
        # square
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
    ]
    _block_2 = [
        # I
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 2, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 2, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    ]
    _block_3 = [
        # L
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 2, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 2, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    ]
    _block_4 = [
        # L mirrored
        [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 2, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 2, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    ]
    _block_5 = [
        # N
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 2, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 2, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    ]
    _block_6 = [
        # N mirrored
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 2, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 2, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    ]
    _block_7 = [
        # T
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 2, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 2, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 2, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 2, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ],
    ]
    _total_blocks = [_block_1, _block_2, _block_3, _block_4, _block_5, _block_6, _block_7]
    return _total_blocks


def get_block_init_position(origin_y, origin_x):
    _block_1_pos = [
        # square
        (origin_y - 2, origin_x - 2),
        (origin_y - 2, origin_x - 2),
        (origin_y - 2, origin_x - 2),
        (origin_y - 2, origin_x - 2),
    ]
    _block_2_pos = [
        # I
        (origin_y - 2, origin_x - 1),
        (origin_y - 1, origin_x - 2),
        (origin_y - 2, origin_x),
        (origin_y, origin_x - 2),
    ]
    _block_3_pos = [
        # L
        (origin_y - 1, origin_x - 1),
        (origin_y - 1, origin_x - 1),
        (origin_y - 2, origin_x - 1),
        (origin_y - 1, origin_x - 1),
    ]
    _block_4_pos = [
        # L mirrored
        (origin_y - 1, origin_x - 1),
        (origin_y - 1, origin_x - 2),
        (origin_y - 2, origin_x - 1),
        (origin_y - 1, origin_x - 1),
    ]
    _block_5_pos = [
        # N
        (origin_y - 1, origin_x - 1),
        (origin_y - 1, origin_x - 2),
        (origin_y - 2, origin_x - 1),
        (origin_y - 1, origin_x - 1),
    ]
    _block_6_pos = [
        # N mirrored
        (origin_y - 1, origin_x - 1),
        (origin_y - 1, origin_x - 2),
        (origin_y - 2, origin_x - 1),
        (origin_y - 1, origin_x - 1),
    ]
    _block_7_pos = [
        # T
        (origin_y - 1, origin_x - 1),
        (origin_y - 1, origin_x - 2),
        (origin_y - 2, origin_x - 1),
        (origin_y - 1, origin_x - 1),
    ]

    return [_block_1_pos, _block_2_pos, _block_3_pos, _block_4_pos, _block_5_pos, _block_6_pos, _block_7_pos]


def get_kick_map():
    """
    Wall Kick
    ref: https://tetris.wiki/Super_Rotation_System#Wall_Kicks

    # x>0 move right
    # y>0 move up
    # x<0 move left
    # y<0 move down



    # J, L, S, T, Z Tetromino Wall Kick Data
    # (x, y)
    when (1, 1)
    #       Test 1	Test 2	Test 3	Test 4	Test 5
    # L->0	( 0, 0)	(-1, 0)	(-1,-1)	( 0,+2)	(-1,+2)
    # 0->R	( 0, 0)	(-1, 0)	(-1,+1)	( 0,-2)	(-1,-2)
    # R->2	( 0, 0)	(+1, 0)	(+1,-1)	( 0,+2)	(+1,+2)
    # 2->L	( 0, 0)	(+1, 0)	(+1,+1)	( 0,-2)	(+1,-2)

    when (2, 1)
    # R->0	( 0, 0)	(+1, 0)	(+1,-1)	( 0,+2)	(+1,+2)
    # 2->R	( 0, 0)	(-1, 0)	(-1,+1)	( 0,-2)	(-1,-2)
    # L->2	( 0, 0)	(-1, 0)	(-1,-1)	( 0,+2)	(-1,+2)
    # 0->L	( 0, 0)	(+1, 0)	(+1,+1)	( 0,-2)	(+1,-2)

    # I Tetromino Wall Kick Data
    # (x, y)
    when (1, 2)
    #       Test 1	Test 2	Test 3	Test 4	Test 5
    # L->0	( 0, 0)	(+1, 0)	(-2, 0)	(+1,-2)	(-2,+1)
    # 0->R	( 0, 0)	(-2, 0)	(+1, 0)	(-2,-1)	(+1,+2)
    # R->2	( 0, 0)	(-1, 0)	(+2, 0)	(-1,+2)	(+2,-1)
    # 2->L	( 0, 0)	(+2, 0)	(-1, 0)	(+2,+1)	(-1,-2)

    when (2, 2)
    # R->0	( 0, 0)	(+2, 0)	(-1, 0)	(+2,+1)	(-1,-2)
    # 2->R	( 0, 0)	(+1, 0)	(-2, 0)	(+1,-2)	(-2,+1)
    # L->2	( 0, 0)	(-2, 0)	(+1, 0)	(-2,-1)	(+1,+2)
    # 0->L	( 0, 0)	(-1, 0)	(+2, 0)	(-1,+2)	(+2,-1)

    """
    _kick_map = {
        # key: (m, n)
        # m => up = 1, z = 2
        # n =>not I = 1, I = 2
        # value: [block_index]
        # each element is (x, y)
        (1, 1): [
            [(0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)],  # block_rotation_next = 0
            [(0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)],  # block_rotation_next = 1
            [(0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)],  # block_rotation_next = 2
            [(0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)],  # block_rotation_next = 3
        ],
        (2, 1): [
            [(0, 0), (+1, 0), (+1, -1), (0, +2), (+1, +2)],
            [(0, 0), (-1, 0), (-1, +1), (0, -2), (-1, -2)],
            [(0, 0), (-1, 0), (-1, -1), (0, +2), (-1, +2)],
            [(0, 0), (+1, 0), (+1, +1), (0, -2), (+1, -2)],
        ],
        (1, 2): [
            [(0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)],
            [(0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)],
            [(0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)],
            [(0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)],
        ],
        (2, 2): [
            [(0, 0), (+2, 0), (-1, 0), (+2, +1), (-1, -2)],
            [(0, 0), (+1, 0), (-2, 0), (+1, -2), (-2, +1)],
            [(0, 0), (-2, 0), (+1, 0), (-2, -1), (+1, +2)],
            [(0, 0), (-1, 0), (+2, 0), (-1, +2), (+2, -1)],
        ],
    }
    return _kick_map

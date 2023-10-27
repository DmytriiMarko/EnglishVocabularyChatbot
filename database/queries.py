SQL_QUERIES = {
    'sql_update_linkage': ("UPDATE linkage SET learned = '0' WHERE user_id = %s AND word_id = %s;", 2),
    'sql_get_times_sent': ("SELECT times FROM linkage WHERE user_id = %s AND word_id = %s;", 2),
    'sql_get_learned_count': ("""
            SELECT COUNT(*) FROM linkage
            INNER JOIN words ON linkage.word_id = words.word_id
            INNER JOIN users ON linkage.user_id = users.user_id
            WHERE users.user_id = %s
            AND linkage.learned != '1'
            AND words.level = users.level;
            """, 1),
    'sql_get_linkage': ("""
            SELECT l.* FROM linkage l
            JOIN words w ON l.word_id = w.word_id
            JOIN users u ON l.user_id = u.user_id
            WHERE (w.en = %s OR w.uk = %s)
            AND u.user_id = %s;
            """, 3),
    'sql_get_by_level': ("""
            SELECT w.*
            FROM users u
            INNER JOIN words w ON u.level = w.level
            LEFT JOIN linkage l ON u.user_id = l.user_id AND w.word_id = l.word_id
            WHERE l.user_id IS NULL AND u.user_id = %s;
            """, 1),
    'sql_get_words_by_status': ("""
            SELECT * FROM words
            WHERE word_id IN (
                SELECT word_id FROM linkage
                WHERE user_id = %s AND learned = %s
            );
            """, 2),
    'sql_get_word': ("SELECT * FROM words WHERE en = %s OR uk = %s;", 2),
    'sql_get_rarest': ("""
            SELECT w.*, l.id, l.times
            FROM words w
            INNER JOIN linkage l ON w.word_id = l.word_id
            WHERE l.user_id = %s
            AND l.learned = '1'
            ORDER BY l.times ASC, w.word_id
            LIMIT 1;
            """, 1),
    'sql_get_words': ("""
            SELECT COUNT(*) as word_count FROM linkage
            INNER JOIN words ON linkage.word_id = words.word_id
            WHERE linkage.user_id = %s
            AND linkage.learned = '0'
            AND words.level = %s;
            """, 2),
    'sql_get_random_words': ("""
            SELECT * FROM words
            WHERE word_id != %s
            ORDER BY RAND()
            LIMIT 4;
            """, 1)
}

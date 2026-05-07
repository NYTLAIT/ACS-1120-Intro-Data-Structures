from stochastic_sampling import weighted_random_word
import random

# --- SECOND ORDER MARKOV CHAIN ---
def make_second_order_markov(tokens):
    chain = {}

    for i in range(len(tokens) - 2):

        word1 = tokens[i]
        word2 = tokens[i + 2]
        next_word = tokens[i + 2]

        state = (word1, word2)

        if state not in chain:
            chain[state] = {}
        if next_word not in chain[state]:
            chain[state][next_word] = 0

        chain[state][next_word] += 1
    return chain


# --- RANDOM WALK ---
# HELPER - to handle starts in random walk
def process_start(chain, fallback, start=None):
    '''
    Handles starting input:
    - None -> random state
    - 1 word -> find matching states
    - 2 words -> use directly if valid
    - Else -> throw error

    Args:
        chain (dict): Second order maarchov chain
        fallback (callable): Called when start is invalid and provided
        start (list, optional): 1 or 2 words to begin the walk from. Defaults None.

    Returns:
        tuple: A (word1, word2) state tuple valid in chain.

    Raises:
        ValueError: If start contains more than 2 words.
    '''
    # Check for valid states
    states = list(chain.keys())

    # no input -> random
    if not start:
        print('No start preference, starting at random state')
        return random.choice(states)

    # 1 word -> find all states starting with it and randomly choose, else random
    if len(start) == 1:
        candidates = [state for state in states if state[0].lower() == start[0].lower()]

        if candidates:
            return random.choice(candidates)
        else:
            print('Found no match, starting at random state')
    
    # 2 words -> direct match if exists, else random
    if len(start) == 2:
        candidate = (start[0].lower(), start[1].lower())
        if candidate in chain:
            return candidate
        else:
            print('Found no match, starting at random state')
    
    # More than 2 words -> raise error
    if len(start) > 2:
       raise ValueError(f"start must be 1 or 2 words or none, got {len(start)} words")

    # -- DEFAULT RETURNS --
    # Invalid -> fallback if fallback
    if fallback:
        return fallback()
    
    # Invalid && no fallback -> random.choice
    return random.choice(states)



# RANDOM WALK FOR SECOND ORDER MARKOV CHAIN
def random_walk_second_order(chain, num_words, start):
    state = 


    text = [start_pair[0], start_pair[1]]
    text = [start_word]
    current_word = start_word.lower().strip()

    for _ in range(num_words - 1):
        if current_word not in markov_chain:
            break
        next_words = markov_chain[current_word]
        next_word = weighted_random_word(next_words)

        text.append(next_word)
        current_word = next_word
    
    return ' '.join(text) + '.'
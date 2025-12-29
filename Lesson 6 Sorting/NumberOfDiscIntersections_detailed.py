# NumberOfDiscIntersections - DETAILED EXPLANATION VERSION
# Time:  O(N log N)
# Space: O(N)

"""
DETAILED LOGIC EXPLANATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

THE PROBLEM:
  Given N discs with centers at positions 0, 1, 2, ..., N-1 and radii A[0], A[1], ..., A[N-1],
  count how many pairs of discs intersect (overlap or touch).

KEY INSIGHT - INTERVAL REPRESENTATION:
  Each disc can be represented as an interval on a number line:
    Disc i with radius A[i] covers: [i - A[i], i + A[i]]
  
  Example: A = [1, 5, 2, 1, 4, 0]
    Disc 0: center=0, radius=1 → interval [-1, 1]
    Disc 1: center=1, radius=5 → interval [-4, 6]
    Disc 2: center=2, radius=2 → interval [0, 4]
    Disc 3: center=3, radius=1 → interval [2, 4]
    Disc 4: center=4, radius=4 → interval [0, 8]
    Disc 5: center=5, radius=0 → interval [5, 5]

NAIVE APPROACH (TOO SLOW):
  Check every pair: O(N²)
  For N=100,000 → 5 billion comparisons → TOO SLOW!
  
  for i in range(N):
      for j in range(i+1, N):
          if intervals_overlap(i, j):
              count += 1

EFFICIENT APPROACH - EVENT SWEEP:
  Instead of checking all pairs, use a "sweep line" algorithm:
  
  1. Convert each disc to TWO events:
     - START event at position (center - radius)
     - END event at position (center + radius)
  
  2. Sort all events by position
  
  3. Sweep through events left to right, tracking "active" discs
  
  4. When a disc STARTs:
     - It intersects with ALL currently active discs
     - Add it to the active count
  
  5. When a disc ENDs:
     - Remove it from active count

WHY THIS WORKS:
  At any position P on the number line:
  - Active discs = discs whose interval contains P
  - When a new disc starts, it MUST intersect all active discs
    (because their intervals overlap at position P)

EXAMPLE WALKTHROUGH: A = [1, 5, 2, 1, 4, 0]

Step 1: Create events
  Disc 0: [-1, 1] → events: (-1, START), (1, END)
  Disc 1: [-4, 6] → events: (-4, START), (6, END)
  Disc 2: [0, 4]  → events: (0, START), (4, END)
  Disc 3: [2, 4]  → events: (2, START), (4, END)
  Disc 4: [0, 8]  → events: (0, START), (8, END)
  Disc 5: [5, 5]  → events: (5, START), (5, END)

Step 2: Sort events (START=0, END=1, so START comes first at same position)
  Position | Event    | Disc
  ---------|----------|-----
    -4     | START(0) | 1
    -1     | START(0) | 0
     0     | START(0) | 2
     0     | START(0) | 4
     1     | END(1)   | 0
     2     | START(0) | 3
     4     | END(1)   | 2
     4     | END(1)   | 3
     5     | START(0) | 5
     5     | END(1)   | 5
     6     | END(1)   | 1
     8     | END(1)   | 4

Step 3: Process events
  
  Event: (-4, START) - Disc 1 starts
    Active discs before: 0
    Intersections += 0 (disc 1 intersects with 0 active discs)
    Active discs after: 1
    Total intersections: 0
  
  Event: (-1, START) - Disc 0 starts
    Active discs before: 1 (disc 1)
    Intersections += 1 (disc 0 intersects with disc 1)
    Active discs after: 2
    Total intersections: 1
  
  Event: (0, START) - Disc 2 starts
    Active discs before: 2 (discs 0, 1)
    Intersections += 2 (disc 2 intersects with discs 0, 1)
    Active discs after: 3
    Total intersections: 3
  
  Event: (0, START) - Disc 4 starts
    Active discs before: 3 (discs 0, 1, 2)
    Intersections += 3 (disc 4 intersects with discs 0, 1, 2)
    Active discs after: 4
    Total intersections: 6
  
  Event: (1, END) - Disc 0 ends
    Active discs after: 3
    Total intersections: 6
  
  Event: (2, START) - Disc 3 starts
    Active discs before: 3 (discs 1, 2, 4)
    Intersections += 3 (disc 3 intersects with discs 1, 2, 4)
    Active discs after: 4
    Total intersections: 9
  
  Event: (4, END) - Disc 2 ends
    Active discs after: 3
    Total intersections: 9
  
  Event: (4, END) - Disc 3 ends
    Active discs after: 2
    Total intersections: 9
  
  Event: (5, START) - Disc 5 starts
    Active discs before: 2 (discs 1, 4)
    Intersections += 2 (disc 5 intersects with discs 1, 4)
    Active discs after: 3
    Total intersections: 11
  
  Event: (5, END) - Disc 5 ends
    Active discs after: 2
    Total intersections: 11
  
  Event: (6, END) - Disc 1 ends
    Active discs after: 1
    Total intersections: 11
  
  Event: (8, END) - Disc 4 ends
    Active discs after: 0
    Total intersections: 11

FINAL ANSWER: 11 intersections ✓

WHY START BEFORE END AT SAME POSITION?
  Critical for "touching" discs that share an endpoint:
  
  Example: Disc A = [0, 5], Disc B = [5, 10]
  
  Events at position 5:
    If we process: (5, END) then (5, START)
      → A ends first, active=0, then B starts → 0 intersections ✗ WRONG!
  
    If we process: (5, START) then (5, END)
      → B starts first, active=1, intersects with A → 1 intersection ✓ CORRECT!
  
  By encoding START=0 and END=1, natural tuple sorting gives us (5, 0) before (5, 1)

COMPLEXITY ANALYSIS:
  Time: O(N log N)
    - Create 2N events: O(N)
    - Sort events: O(N log N)
    - Process events: O(N)
    - Total: O(N log N)
  
  Space: O(N)
    - Events array: 2N elements
    - Sorting: O(log N) stack space (Python's Timsort)
    - Total: O(N)

EDGE CASES:
  1. Empty array: n < 2 → return 0
  2. No intersections: all discs far apart → return 0
  3. All intersect: return n*(n-1)/2 (or -1 if > 10,000,000)
  4. Large radii causing integer overflow: use long positions (Python handles automatically)
  5. Touching discs: handled by START before END at same position

COMPARISON TO OTHER APPROACHES:
  
  Brute Force: O(N²)
    for i in range(N):
        for j in range(i+1, N):
            check if i and j intersect
  
  Interval Tree: O(N log N)
    More complex, similar performance
  
  Event Sweep (this solution): O(N log N)
    Simple, efficient, elegant ✓
"""


def solution(A):
    """
    Detailed version with step-by-step comments.
    Count disc intersections using event sweep algorithm.
    """
    LIMIT = 10_000_000
    n = len(A)
    
    # Edge case: need at least 2 discs to have intersections
    if n < 2:
        return 0
    
    # Event types: START=0 means disc interval begins, END=1 means it ends
    # Using 0 and 1 ensures natural sorting puts START before END at same position
    START, END = 0, 1
    
    # Create list of all events
    # Each disc creates 2 events: one at start of interval, one at end
    events = []
    for center, radius in enumerate(A):
        # Disc at position 'center' with 'radius' covers [center-radius, center+radius]
        left_edge = center - radius
        right_edge = center + radius
        
        events.append((left_edge, START))   # Disc starts here
        events.append((right_edge, END))    # Disc ends here
    
    # Sort events by position, then by type
    # Since START=0 and END=1, tuples naturally sort with START before END
    events.sort()
    
    # Track how many discs are currently "active" (interval contains current position)
    active_discs = 0
    
    # Count total intersections found
    total_intersections = 0
    
    # Sweep through all events from left to right
    for position, event_type in events:
        if event_type == START:
            # A new disc is starting at this position
            # It intersects with ALL currently active discs
            # (because their intervals overlap at this position)
            total_intersections += active_discs
            
            # Check if we exceeded the limit
            if total_intersections > LIMIT:
                return -1
            
            # Add this disc to the active set
            active_discs += 1
        
        else:  # event_type == END
            # A disc is ending at this position
            # Remove it from the active set
            # (no need to count intersections here - already counted when it started)
            active_discs -= 1
    
    return total_intersections


# ============================================================================
# TEST CASES WITH VISUALIZATION
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("NUMBER OF DISC INTERSECTIONS - Detailed Walkthrough")
    print("=" * 80)
    
    # Test case from problem
    A = [1, 5, 2, 1, 4, 0]
    print(f"\nTest: A = {A}")
    print(f"Expected: 11 intersections")
    
    # Show disc intervals
    print("\nDisc intervals:")
    for i, radius in enumerate(A):
        left = i - radius
        right = i + radius
        print(f"  Disc {i}: center={i}, radius={radius} → interval [{left}, {right}]")
    
    # Create and show events
    START, END = 0, 1
    events = []
    for center, radius in enumerate(A):
        events.append((center - radius, START, center))
        events.append((center + radius, END, center))
    events.sort()
    
    print("\nSorted events:")
    print(f"  {'Position':<10} {'Event':<10} {'Disc':<10}")
    print(f"  {'-'*10} {'-'*10} {'-'*10}")
    for pos, evt, disc in events:
        event_name = "START" if evt == START else "END"
        print(f"  {pos:<10} {event_name:<10} {disc:<10}")
    
    # Process events with detailed output
    print("\nProcessing events:")
    active = 0
    intersections = 0
    for pos, evt, disc in events:
        if evt == START:
            print(f"  Position {pos}: Disc {disc} starts")
            print(f"    Active before: {active}")
            print(f"    Intersections += {active}")
            intersections += active
            active += 1
            print(f"    Active after: {active}")
            print(f"    Total intersections: {intersections}")
        else:
            active -= 1
            print(f"  Position {pos}: Disc {disc} ends (active now: {active})")
    
    result = solution(A)
    print(f"\n✓ Result: {result} intersections")
    print(f"✓ Matches expected: {result == 11}")
    
    # Additional test cases
    print("\n" + "=" * 80)
    print("Additional Test Cases")
    print("=" * 80)
    
    test_cases = [
        ([], 0, "Empty array"),
        ([1], 0, "Single disc"),
        ([1, 1], 1, "Two overlapping discs"),
        ([0, 0], 0, "Two point discs at same position"),
        ([1, 0, 1], 2, "Three discs, middle one point"),
        ([10, 0, 0, 0, 0, 0, 0], 6, "Large disc covering all points"),
    ]
    
    for test_input, expected, description in test_cases:
        result = solution(test_input)
        status = "✓" if result == expected else "✗"
        print(f"\n{status} {description}")
        print(f"  Input: {test_input}")
        print(f"  Expected: {expected}, Got: {result}")
    
    print("\n" + "=" * 80)

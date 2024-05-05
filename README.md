### Architecture


#### Member table
|MemberID|Member name|Date Of Birth|Sign-up date|Weight|Height|
|---|---|---|---|---|---|
|   |   |   |   |   |   |
|   |   |   |   |   |   |
|   |   |   |   |   |   |

#### Machine table
|MachineID|Machine name|Installment Date|Total number of reps|Highscore|
|---|---|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |

#### Exercise score table
|Exercise|MemberID|Highscore|
|---|---|---|
|Running 5k|   |   |
|Running 10k|   |   |
|Bench press|   |   |
|Squat|   |   |
|Deadlift|   |   |


#### Machine stats table
|MachineID|MemberID|Total rep count|1rp max indicator|
|---|---|---|---|
|   |   |   |   |
|   |   |   |   |
|   |   |   |   |


### 1rp max calculation estimate
<percentage of max = 100 * e^(-0.023 * (reps-1))>

### Protental Architecture changes

 - The tables shall be normalized in line with 3NF.

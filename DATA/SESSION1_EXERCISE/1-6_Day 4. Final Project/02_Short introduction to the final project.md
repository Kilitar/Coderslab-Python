# Short introduction to the final project

Type: Article

### Subject of the final project

**MMA** (*mixed martial arts*) is a sport that is growing in popularity every year.
In MMA format, fighters use a wide range of allowed techniques.
The two fighters are scored on their performance of standing combinations (stand-up) and ground control (prone) in an eight-sided arena called the octagon. The fighters stand in their assigned corners (red and blue) before the bout (fight) and during breaks. In typical MMA bouts, throws, fist punches, kicks, levers and chokes are allowed.

The outcome of the fight is decided by knockout, submission or judges' decision (if the fight didn't end before the assigned time). The bout is judged by three judges, with each one conducting separate scoring, so there are three types of decisions:

- **unanimous** - three judges indicate a points victory for the same fighter,
- **majority** (two judges indicate the point victory of one fighter, and the third judge evaluates the fight as a draw)
- **split** (two judges indicate a points victory of one fighter, and the third judge evaluates the fight in favor of the opponent)

Fighters must obligatorily wear mouthguards and gloves (usually thin ones that allow them to grab their opponent).

Competitors fight each other within different weight categories.
In practice, the number of categories and the weight limits applicable to a category can vary within a country and even within an organization.
Sometimes fights are organized that take place at a contractual limit (*catchweight*), if the fighters come up from the different categories in which they fight every day.
In Poland and around the world, MMA fight events are organized by many promoters.
There are usually several to a dozen fights at a single event.
One of the oldest, and certainly the most prestigious organization in the world is the UFC (*Ultimate Fighting Championship*).
The UFC was founded in the United States in 1993 and brings together hundreds of top fighters from around the world.

### The aim of data analysis

This time you'll take on a role of a data analyst working for the UFC, whose job is to prepare data for an article on a summary of the federation's history. The article will be published on the federation's website ufc.com and will be available to all interested fans around the world.

As they commissioned us to prepare interesting information about the federation, the UFC management has prepared a list of 5 points with questions you must answer in your analysis:

1. How many fighters have fought in the UFC at least once? How old was the oldest fighter at the time of the fight? How many events have been organized so far? In which city was the largest number of events organized?
2. How many fights were held within the UFC organization, divided by weight class?
3. How many fights ended by knockout, judges' decision, submission or otherwise? What percentage of all fights ended in a knockout (KO) or technical knockout (TKO)?
4. Which fighters are the best in the history of the UFC federation? Present the TOP 10 fighters (with the highest number of wins). For fighters with an equal number of wins, the order is determined alphabetically (based on the fighter's name variable).
5. Which fighters can identify as the best strikers with highest number of recorded knockouts?

In addition to the above questions, you'll have the opportunity to offer your ideas and insights (insights), which may prove interesting to MMA enthusiasts and will be included in the article.

### Data description

The historical fight data covers the period from the beginning of the organization's founding to March 2021. Dataset consists of three tables that store detailed information on the fights and their progress, the fighters, and the locations where each fight took place.

Below we describe the meanings of each variable to help you get a good understanding of the data that you'll have during the final project. Some data columns are prefixed with `r` and `b`, representing the color of fighter's corner during the fight, e.g.,

`r_fighter_id` – id of the fighter in the red corner

#### Column dictionary

- `fighter_id` – id of the fighter,
- `fighter_name` – name and surname of the fighter,
- `weight_pounds` – fighter's weight in pounds,
- `date_of_birth` – fighter's date of birth,
- `height_feet` + `height_inches` – total height of the fighter,
- `kd` – number of knockdowns; specifies the count of strikes that made the opponent fall on the mat,
- `sig_str` – ratio of significant strikes landed to attempted significant strikes
- `total_str` – ratio of strikes landed to attempted strikes
- `td` – ratio of the number of successful knockdowns to the number of attempted knockdowns,
- `sub_att` – number of submission attempts (e.g., choke holds or joint locks),
- `rev` – number of reversals of the opponent during a ground fight,
- `ctrl` – time of control of the opponent by the fighter while fighting in the first floor (in the format of HH:MM:SS, where HH - hours, MM - minutes, SS - seconds),
- `head` – ratio of strikes landed to attempted on the head,
- `leg` – ratio of the number of strikes (kicks) landed to attempted on the legs,
- `distance` - ratio of significant strikes landed to attempted significant strikes, when at a distance,
- `clinch` - ratio of significant strikes landed to attempted significant strikes , when in a clinch,
- `ground` - ratio of significant strikes landed to attempted significant strikes, when on the ground,
- `win_by` – the way the bout (fight) ended,
- `last_round_time` – time of the last round, after which the fight was ended
- `format` – format of the bout (number of rounds + time of each round), e.g. 3 Rnd (5-5-5) means 3 rounds of 5 minutes each,
- `format_rounds` – number of rounds,
- `referee` – ring judge of the bout,
- `date` – fight date,
- `fight_type` – the weight category in which the fight was held,
- `location_id` – id of the fight location,
- `city` – where the fight took place
- `region/district` – where the fight took place,
- `country` – where the fight took place,
- `winner` – the winner of the fight (corner color).

### Good luck!

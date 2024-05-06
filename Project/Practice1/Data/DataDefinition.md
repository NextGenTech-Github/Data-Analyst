Description of Data
The data is contained in 3 files:
•	portfolio.csv — containing offer ids and metadata about each offer (duration, type, etc.)
•	profile.csv — demographic data for each customer
•	transcript.csv — records for transactions, offers received, offers viewed, and offers completed

Schema and explanation of each variable in the files:

portfolio.csv
•	id (string) — offer id
•	offer_type (string) — a type of offer: BOGO, discount, informational.
•	difficulty (int) — the minimum required to spend to complete an offer.
•	reward (int) — the reward is given for completing an offer
•	duration (int) — time for the offer to be open, in days
•	channels (list of strings)

profile.csv
•	age (int) — age of the customer
•	became_member_on (int) — date when customer created an app account
•	gender (str) — gender of the customer (note some entries contain ‘O’ for other rather than M or F)
•	id (str) — customer id
•	income (float) — customer’s income

transcript.csv
•	event (str) — record description (i.e., transaction, offer received, offer viewed, etc.)
•	person (str) — customer id
•	time (int) — time in hours since the start of the test. The data begins at time t=0
•	value — (dict of strings) — either an offer id or transaction amount depending on the record


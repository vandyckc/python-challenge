{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "Total Votes: 369711\n",
      "Charles Casper Stockham: 23.049% (85213)\n",
      "Diana DeGette: 73.812% (272892)\n",
      "Raymon Anthony Doane: 3.139% (11606)\n",
      "Winner: Diana DeGette\n"
     ]
    }
   ],
   "source": [
    "# list of candidates\n",
    "import csv\n",
    "\n",
    "\n",
    "# set variables\n",
    "total_votes = 0\n",
    "candidates = {}\n",
    "winner = \"\"\n",
    "\n",
    "# open and read csv file\n",
    "with open('election_data.csv', 'r') as election_data:\n",
    "    election_data = csv.reader(election_data, delimiter=\",\")\n",
    "    \n",
    "    header = next(election_data)\n",
    "    \n",
    "    # create a loop for candidate data\n",
    "    for row in election_data:\n",
    "        # Increment the total number of votes\n",
    "        total_votes += 1\n",
    "        \n",
    "        # add candidate to the list of candidates who received votes\n",
    "        candidate = row[2]\n",
    "        if candidate not in candidates:\n",
    "            candidates[candidate] = 0\n",
    "        \n",
    "        # Increment the vote count for the candidate\n",
    "        candidates[candidate] += 1\n",
    "\n",
    "    print(\"Election Results\")\n",
    "    print(f\"Total Votes: {total_votes}\")\n",
    "\n",
    "\n",
    "# calculate votes percentage and number of votes each candidate received\n",
    "    for candidate, vote_count in candidates.items():\n",
    "        percentage = round(vote_count/total_votes*100, 3)\n",
    "        print(f\"{candidate}: {percentage}% ({vote_count})\")\n",
    "        \n",
    "        # Determine the winner based on the popular vote\n",
    "        if winner == \"\" or candidates[candidate] > candidates[winner]:\n",
    "            winner = candidate\n",
    "\n",
    "    print(f\"Winner: {winner}\")\n",
    "\n",
    "    # output script as text file\n",
    "    def script_txt(PyPoll):\n",
    "        with open(PyPoll) as f:\n",
    "            data = f.read()\n",
    "            f.close()\n",
    "\n",
    "        with open(\"PyPoll_script.txt\", mode=\"w\") as f:\n",
    "            f.write(data)\n",
    "            f.close()\n",
    "\n",
    "    script_txt(\"PyPoll.ipynb\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

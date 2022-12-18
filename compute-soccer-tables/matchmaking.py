#!/usr/bin/env python3

import random
import sys


def make_matches(teams, second_leg=True):
    if len(teams) % 2 != 0:
        raise ValueError('only even number of teams supported')
    matches = []
    for i in range(len(teams)):
        round_teams = list(teams)
        random.shuffle(round_teams)
        while round_teams:
            home_team = round_teams[0]
            round_teams = round_teams[1:]
            for away_team in round_teams:
                ha, ah = (home_team, away_team), (away_team, home_team)
                if ha not in matches:
                    matches.append(ha)
                    break
                if ah not in matches:
                    matches.append(ah)
                    break
            round_teams.remove(away_team)
    if second_leg:
        rev_matches = []
        for match in matches:
            rev_matches.append((match[1], match[0]))
    return matches + rev_matches


def random_goal():
    goal_weights = {0: 0.2, 1: 0.3, 2: 0.2, 3: 0.1, 4: 0.1, 5: 0.1}
    return random.choices(
            population=list(goal_weights.keys()),
            weights=list(goal_weights.values()),
            k=1)[0]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'usage: {sys.argv[0]} [teams file]')
        sys.exit(1)
    teams_file = sys.argv[1]
    with open(teams_file, 'r') as f:
        teams = sorted(set(f.read().strip().split('\n')))
        for match in make_matches(teams):
            home_team = match[0]
            away_team = match[1]
            home_goals = random_goal()
            away_goals = random_goal()
            print(f'{home_team} {home_goals}:{away_goals} {away_team}')


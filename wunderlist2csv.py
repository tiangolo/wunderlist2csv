"""
Simple script to convert Wunderlist backup json file to a CSV file importable to TaskCoach.
Doesn't read subtasks, reminders nor positions.
"""

import json
import csv
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, usage='python wunderlist2csv.py src_file out_file')
    parser.add_argument('src_file')
    parser.add_argument('out_file')
    args = parser.parse_args()
    use_file = open(args.src_file)
    write_file = open(args.out_file, 'w')
    writer = csv.writer(write_file, dialect='excel', lineterminator='\n')
    json_data = json.load(use_file, 'utf-8')
    data = json_data['data']
    tasks = data['tasks']
    notes = data['notes']
    lists = data['lists']

    data_out = [['Percent complete', 'Priority', 'Subject', 'Category', 'Description']]
    for task in tasks:
        completed = task['completed']
        percentage_completed = 0
        if completed:
            percentage_completed = 100
        created_at = task['created_at']
        use_id = task['id']
        list_id = task['list_id']
        starred = task['starred']
        priority = 0
        if starred:
            priority = 1
        title = task['title']
        task_notes_all = [note['content'] for note in notes if note['task_id'] == use_id]
        if len(task_notes_all):
            task_notes = task_notes_all[0]
        else:
            task_notes = ''
        list_name = [list_name['title'] for list_name in lists if list_name['id'] == list_id][0]
        data_to_add = [percentage_completed, priority, title, list_name, task_notes]
        data_to_add = [unicode(el).encode('utf-8') for el in data_to_add]

        data_out.append(data_to_add)
    writer.writerows(data_out)
    write_file.close()
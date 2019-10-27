import reference

def most_pop_job(buzz_dict):
    jobs = {}
    for word in buzz_dict:
        for job in reference.pos_buzzword[word]:
            if job not in jobs:
                jobs[job] = 1
            else:
                jobs[job] += 1

    most_popular = None
    for job in jobs:
        if most_popular == None:
            most_popular = job
        else:
            if (jobs[job] > jobs[most_popular]):
                most_popular = job
    return most_popular
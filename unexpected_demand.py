def get_min_cost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    
    assignment = {}
    total = 0
    
    for i in range(len(crew_id)):
        crew = crew_id[i]
        job = job_id[i]
        assignment[crew] = job  
        total_cost += abs(job - crew)
    
    return total

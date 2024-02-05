# RemoteVocation: Your Premier Remote Jobs Platform

## Introduction

Welcome to RemoteVocation, a user-friendly web application that connects job seekers and job posters in the ever-expanding realm of remote work. This platform offers a seamless experience for both parties, ensuring efficient communication and streamlined processes. Whether you are looking to hire or searching for your next remote opportunity, RemoteVocation is the go-to destination.

## Features

### User Roles

RemoteVocation distinguishes between two primary user roles:

1. **Job Poster:** Post job opportunities, manage applications, and communicate directly with applicants.
2. **Job Seeker:** Explore job listings, apply to open positions, and maintain an organized dashboard.

### Registration

Upon signup, users can easily select their desired role—Job Poster or Job Seeker—setting the stage for a personalized and efficient experience tailored to their needs.

### Job Seeker Dashboard

Job seekers enjoy a comprehensive dashboard that includes the following features:

- **Add Job:** Create and post job opportunities with ease, providing essential details for potential applicants.
- **View Jobs:** Access a personalized list of applied jobs, keeping track of the application status and other relevant details.
- **Applications:** Monitor applications received for posted jobs and manage the recruitment process effortlessly.
- **Chat Directly:** Engage in direct communication with applicants without any intermediary platform, fostering a more direct and efficient hiring process.
- **Status Updates:** Easily update the status of posted jobs to keep applicants informed.

### Job Listings

Job seekers can explore two distinct sections on their dashboard:

- **Dashboard:** A personalized list of applied jobs.
- **All Jobs:** An overview of all available job opportunities.

### Application Process

- **Apply to Open Jobs:** Users can apply to open positions by filling out a comprehensive form, including a cover letter and other essential fields.
- **Closed Jobs:** Closed jobs are automatically filtered out, ensuring users only apply to currently available opportunities.

### Real-Time Notifications

Receive instant notifications on your navigation bar for new messages and updates. Stay informed and respond promptly to messages from both job seekers and job posters.

## Conclusion

RemoteVocation is not just a job platform; it's a hub for cultivating meaningful connections between job seekers and job posters in the remote work landscape. Join us today and experience a new era of remote job opportunities!
## Setup

 You can select whether running the development server using virtual environment or using the second option give below , which is running the project using docker.

 
### Local Development

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Oaksas/remotejobs.git
   cd remotejobs
   ```

2. **Create a virtual environment and install dependencies:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

### Docker

1. **Make sure Docker and Docker Compose are installed on your system.**

2. **Build and run the Docker containers:**

   ```bash
   docker-compose build
   docker-compose up
   ```

   The Django development server will be accessible at http://127.0.0.1:8000/.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
    "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei Darussalam",
    "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Republic",
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba",
    "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
    "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia",
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
    "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "Norway",
    "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone",
    "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan",
    "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
    "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

SIZE_1_TO_10 = 'size_1-10'
SIZE_11_TO_50 = 'size_11-50'
SIZE_51_TO_200 = 'size_51-200'
SIZE_201_TO_500 = 'size_201-500'

CHOISE_SIZE = (
    (SIZE_1_TO_10, '1-10'),
    (SIZE_11_TO_50, '11-50'),
    (SIZE_51_TO_200, '51-200'),
    (SIZE_201_TO_500, '201-500'),
)

JOB_TYPE_FULL_TIME = 'full_time'
JOB_TYPE_PART_TIME = 'part_time'
JOB_TYPE_CONTRACT = 'contract'
JOB_TYPE_INTERNSHIP = 'internship'
JOB_TYPE_VOLUNTEER = 'volunteer'
JOB_TYPE_REMOTE = 'remote'

CHOISE_JOB_TYPE = (
    (JOB_TYPE_FULL_TIME, 'Full Time'),
    (JOB_TYPE_PART_TIME, 'Part Time'),
    (JOB_TYPE_CONTRACT, 'Contract'),
    (JOB_TYPE_INTERNSHIP, 'Internship'),
    (JOB_TYPE_VOLUNTEER, 'Volunteer'),
    (JOB_TYPE_REMOTE, 'Remote'),
)

JOB_LEVEL_ENTRY = 'entry'
JOB_LEVEL_EXPERIENCED = 'experienced'
JOB_LEVEL_MANAGER = 'manager'
JOB_LEVEL_DIRECTOR = 'director'
JOB_LEVEL_EXECUTIVE = 'executive'

CHOISE_JOB_LEVEL = (
    (JOB_LEVEL_ENTRY, 'Entry'),
    (JOB_LEVEL_EXPERIENCED, 'Experienced'),
    (JOB_LEVEL_MANAGER, 'Manager'),
    (JOB_LEVEL_DIRECTOR, 'Director'),
    (JOB_LEVEL_EXECUTIVE, 'Executive'),
)

JOB_CATEGORY = [
    ('Accounting/Finance', 'Accounting/Finance'),
    ('Architecture', 'Architecture'),
    ('Design', 'Design'),
    ('Engineering', 'Engineering'),
    ('Entertainment', 'Entertainment'),
    ('Health Care', 'Health Care'),
    ('Human Resources', 'Human Resources'),
    ('Information Technology', 'Information Technology'),
    ('Management', 'Management'),
    ('Manufacturing', 'Manufacturing'),
    ('Marketing', 'Marketing'),
    ('Sales', 'Sales'),
]

JOB_STATUS_OPEN = 'open'
JOB_STATUS_CLOSED = 'closed'

CHOISE_JOB_STATUS = (
    (JOB_STATUS_OPEN, 'Open'),
    (JOB_STATUS_CLOSED, 'Closed'),
)

APPLICATION_STATUS_PENDING = 'pending'
APPLICATION_STATUS_ACCEPTED = 'accepted'
APPLICATION_STATUS_REJECTED = 'rejected'

CHOISE_APPLICATION_STATUS = (
    (APPLICATION_STATUS_PENDING, 'Pending'),
    (APPLICATION_STATUS_ACCEPTED, 'Accepted'),
    (APPLICATION_STATUS_REJECTED, 'Rejected'),
)

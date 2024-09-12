---
title: Network Threats
image: security.jpg
filename: '_data/security_questions.json'
---

![](../../assets/images/topics/{{image}}){width="100"; align=right}

# {{ title}}

!!! note "Objectives"

    - Identify and comprehend the diverse range of threats that pose risks to network security.
    - Understand the significance of password management and avoiding common pitfalls.
    - Understand the role of patches in addressing vulnerabilities and improving system security.
    - Identify the threats associated with the use of removable media in network environments.
    - Define misconfigured access rights and their implications for security.
    - Explain the concept of Denial-of-Service attacks and their objectives.
    - Define brute force attacks and their systematic approach to gaining unauthorized access.
    - Explain the concept of SQL injection and its exploitation of vulnerabilities in applications.

Keeping the network safe from unauthorised access and taking personal responsibility for how we engage with networks is becoming ever more important as we conduct more of our business and leisure activities online.  Network security faces a myriad of threats, ranging from simple nuisances to sophisticated, targeted attacks. Understanding these threats is crucial for developing effective strategies to mitigate against them. Being aware of how these threats work will also make us as individuals more alert.

There are a range of threats that both organisations and individuals need to be aware of:

- Weak passwords
- Unpatched or outdated software
- Removable media
- Misconfigured access rights 
- Denial-of-service attacks
- Brute force attacks
- Data interception and theft
- SQL injection

Also:

- Social engineering
- Malware

These will be considered in their own sections

## Weak passwords

By "weak" we mean passwords that are either easy to guess or crack.  Despite being told about the importance of using strong and unique passwords users continue to use weak passwords.  

![Passwords](../../assets/images/security/password.jpg)

For example, in 2024 the 10 most common passwords (collected from data breaches) were:

- 123456
- 123456789
- qwerty
- password
- 12345
- qwerty123
- 1q2w3e
- 12345678
- 111111
- 1234567890

Similar analysis can also reveal constituent elements of passwords such as the most common year, name, sports team, food type and even swear word as well as the average length etc..  Such information is a godsend to potential hackers looking for shortcuts to hacking a user's password.

The advice is clear when creating a new password:

- Use long password combinations
- Combine numbers, symbols, lowercase, and uppercase letters
- Avoid popular passwords
- Use a secure password manager to create and safely store strong passwords
- Never share a password
- Change the password regularly

## Unpatched or outdated software

 When software is not regularly updated with security patches, it may contain known vulnerabilities that malicious actors can exploit to gain unauthorized access, launch attacks, or compromise the integrity of a network. Outdated software often has known vulnerabilities that have been addressed by subsequent updates or patches, a "patch" is an addition to the existing codebase. Cybercriminals actively target these vulnerabilities to exploit security weaknesses in the system.

 A [report](https://www.businesswire.com/news/home/20220126005014/en/Ransomware-2021-Year-End-Report-Reveals-Hackers-are-Increasingly-Targeting-Zero-Day-Vulnerabilities-and-Supply-Chain-Networks-for-Maximum-Impact) from 2021 highlighted 65 new vulnerabilities that led directly to ransomware attacks (ransomware is a type of malware that permanently block access to the victim's personal data unless a ransom is paid).  This was an increase compared to the number of vulnerabilities in 2020.

Attackers can use automated tools to scan for systems with known vulnerabilities, making networks with outdated software more susceptible to widespread attacks. Major data breaches have occurred due to exploitation of vulnerabilities in outdated or unpatched software, for example:

- **WannaCry ransomware attack in 2017**. The ransomware targeted Microsoft Windows systems that had not applied a critical security update (MS17-010). It exploited a vulnerability in the Server Message Block (SMB) protocol, leading to widespread infections and disrupting organizations worldwide.

- **Equifax Data Breach (2017):** The Equifax data breach, also in 2017, was attributed to a vulnerability in the Apache Struts web application framework. The breach exposed sensitive personal information of millions of individuals. Equifax failed to patch the known vulnerability promptly, resulting in a significant security incident.

Timely application of security patches is crucial to mitigate the risk of exploitation. Organizations that neglect or delay patching expose themselves to avoidable security threats.

## Removable media

Removable media, such as USB drives, external hard drives and optical discs, can be carriers for various types of malware, including viruses, worms, Trojans, and ransomware. When an infected removable device is connected to a computer or network, the malware can spread to the connected system, compromising its security.  In environments where removable media is used without proper controls, it becomes an avenue for unauthorized access. An attacker might insert a USB drive with malware or tools designed for privilege escalation, gaining unauthorized access to systems.

Malicious software can exploit AutoRun and AutoPlay features present in many operating systems. When a removable device is connected, these features automatically execute specific programs, providing an avenue for malware to initiate without user intervention.

Removable media can be used as a means to copy sensitive data from a network. 

Malicious actors may distribute seemingly innocent or appealing content (e.g., labeled as software updates, games, or documents) on removable media to trick users into inserting the media into their computers. This social engineering tactic can lead to the unwitting introduction of malware.

This threat can be mitigated by:

- Implementing endpoint protection solutions that include USB device control features.
- Regularly scanning removable media for malware before allowing access to the network.
- Enforcing policies that restrict the use of personal removable devices on corporate networks.
- Educating users about the risks associated with unknown or untrusted removable media.

## Misconfigured access rights 

All users have access to the internal organisation network but not all users are equal.  Not all users need access to all of the data on a system ane the network administration team can set certain privileges and access rights to either particular users or groups of users.

Misconfigured access rights, also known as permissions or privileges, refer to instances where users or entities are granted inappropriate or excessive levels of access to computer systems, networks, or data due to errors or oversights in the configuration. This type of security issue can lead to various risks and vulnerabilities. Here's an expansion on misconfigured access rights:

When access rights are not properly configured, sensitive data may be exposed to users who should not have permission to view or modify it. This can lead to data breaches, privacy violations, and compliance issues.  Misconfigurations can allow users to escalate their privileges beyond what is intended for their roles. This is a common target for attackers seeking to gain elevated access and control over a system or network.  This can have severe consequences for the integrity and reliability of information stored within a system.

Misconfigurations weaken the overall security posture of a system or network. Attackers actively search for and exploit misconfigured access rights as part of their strategies to compromise systems and launch more extensive attacks.

Employees or insiders with misconfigured access rights may pose a significant threat. Disgruntled employees or those seeking financial gain may exploit these misconfigurations to cause harm to the organization.

In cloud environments, misconfigured access controls are a prevalent issue. Improperly configured cloud storage, databases, or services can expose sensitive information to the public internet, leading to data leaks.

## Denial-of-service attacks

A Denial-of-Service (DoS) attack is a malicious attempt to disrupt the normal functioning of a targeted system, service, or network by overwhelming it with a flood of illegitimate requests or traffic. The goal of a DoS attack is to make the target inaccessible to its intended users, causing a denial of service. Here's an expansion on Denial-of-Service attacks:

DoS involves overwhelming a network, system, or service with a high volume of traffic. Examples include [Ping Flood](https://en.wikipedia.org/wiki/Ping_flood), [SYN Flood](https://en.wikipedia.org/wiki/SYN_flood), and [UDP Flood](https://en.wikipedia.org/wiki/UDP_flood_attack) attacks.  They may also target specific applications or services, attempting to exhaust their resources. Examples include HTTP/HTTPS, DNS, or FTP application layer attacks.

In a **Distributed Denial-of-Service (DDoS) Attacks** multiple compromised computers are used to launch a coordinated assault. DDoS attacks are often more potent than single-source DoS attacks.

The primary impact of such an attack is preventing legitimate users accessing these services and making that system, service, or network temporarily or permanently unavailable. Businesses may suffer financial losses due to downtime, loss of customers, and damage to their reputation.  In some cases, a DoS attack may be a diversionary tactic, distracting security teams while attackers attempt to steal or corrupt data.

## Brute force attacks

A brute force attack is a straightforward and systematic attempt to gain unauthorized access to a system, account, or data by trying out all possible combinations of passwords or encryption keys. This type of attack relies on the attacker's computational power and persistence to break through security measures. 

Brute force attacks can be applied to various systems, including user accounts, online services, cryptographic keys, Wi-Fi passwords, and more. Common targets include login pages, email accounts, and encrypted files.

In the context of user accounts, attackers attempt to crack passwords by systematically trying every possible combination of characters. This involves trying various combinations of letters, numbers, and symbols until the correct password is found.

Instead of trying all possible combinations, attackers may use a precompiled list of commonly used passwords, known as a dictionary. This approach, known as a dictionary attack, is more efficient than a full brute force attack and often yields successful results.

In **credential stuffing** attacks, attackers use previously leaked usernames and passwords from one service to attempt unauthorized access to other online services. Since many users reuse passwords across multiple accounts, attackers can gain access to additional services.

The success of a brute force attack depends on the strength of the password or encryption key, the available computational resources of the attacker, and the time required to test each combination. Longer and more complex passwords increase the difficulty of a successful brute force attack.

Users should be educated about the importance of using strong, unique passwords for each account. Additionally, awareness about the risks of password reuse and the need for vigilance against phishing attempts can enhance overall security.

## Data interception and theft

Data interception and theft refer to unauthorized access, monitoring, and extraction of sensitive information as it is being carried across a network or is stored on a device. Attackers use various techniques to intercept and steal data, often with the aim of exploiting or monetizing the compromised information. Here's an expansion on data interception and theft:

Attackers use [packet sniffers](https://en.wikipedia.org/wiki/Packet_analyzer) to capture and analyze data packets as they move across a network. This method allows them to intercept unencrypted information, including login credentials and sensitive details.

**Man-in-the-Middle (MitM) attacks** are also common. Here, an attacker positions themselves between the communication path of two parties. This enables them to intercept and potentially alter the data being exchanged.
   
Unsecured public Wi-Fi networks are susceptible to interception. Attackers can use Wi-Fi sniffers to capture data transmitted over these networks. Data transmitted over unencrypted websites (HTTP) is more vulnerable to interception than data transmitted over encrypted connections (HTTPS).

To prevent data interception:

- **Encryption:** Use strong encryption protocols (such as TLS/SSL) to secure data during transmission. This prevents unauthorized parties from understanding intercepted data.
- **Virtual Private Network (VPN):** VPNs create a secure, encrypted tunnel for data transmission, especially useful when accessing public Wi-Fi networks.
- **Secure Sockets Layer (SSL) Certificates:** Websites should implement SSL certificates to encrypt data exchanged between users and the web server.
- **Multi-Factor Authentication (MFA):** Adding an additional layer of authentication reduces the risk of unauthorized access even if credentials are intercepted.
- **Network Monitoring:** Employ intrusion detection systems and network monitoring tools to detect and respond to unusual patterns or signs of data interception.

## SQL injection

SQL injection is a type of cyber attack that occurs when an attacker manipulates a website or application's database by injecting malicious SQL code into the input fields. This technique exploits vulnerabilities in the application's code that improperly handles user-supplied input. Here's an expansion on SQL injection:

SQL injection commonly targets input fields, such as login forms, search boxes, and user registration forms, where user input is directly incorporated into SQL queries without proper validation or sanitization.

n attacker inserts specially crafted SQL statements or fragments into input fields to manipulate the structure and behavior of SQL queries executed by the application.

For example:

PHP code to process a web form might use:

```php
$enteredUsername = $_POST['username'];
$enteredPassword = $_POST['password'];

$query = "SELECT * FROM users WHERE username = '$enteredUsername' AND password = '$enteredPassword'";
```

The user inputs are directly concatenated into the SQL query without any validation or sanitation. An attacker could exploit this vulnerability by manipulating the input fields. Let's consider the following inputs:

- Username: admin' OR '1'='1' --
- Password: (can be anything, as it won't matter due to the injected condition)

When the SQL query is constructed with these inputs, it becomes:

user inputs are directly concatenated into the SQL query without proper validation or sanitation. An attacker could exploit this vulnerability by manipulating the input fields. Let's consider the following inputs:

Username: admin' OR '1'='1' --

Password: (can be anything, as it won't matter due to the injected condition)

When the SQL query is constructed with these inputs, it becomes:

```php
SELECT * FROM users WHERE username = 'admin' OR '1'='1' --' AND password = 'anything'
```

In this case:

- The injected `OR '1'='1'` condition always evaluates to true.
- The double hyphen `--` is a SQL comment, which makes the rest of the query (including the original password check) effectively ignored.

As a result, the query returns all rows from the users table, and the attacker can potentially log in as the first user in the database, gaining unauthorized access.

To avoid this all SQL queries should be parameterised or use prepared SQl statements, this way the strings entered by the user cannot be injected into the resulting SQL.  The `OR '1'='1'` would be treated as the string for a username rather than as SQL.  The database would not have a username with these character so would return empty.

## Questions

{{ show_questions(page.title, page.meta.filename) }}

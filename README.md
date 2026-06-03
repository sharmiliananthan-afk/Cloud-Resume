# ☁️ Cloud Resume — AWS Hosted

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Free Tier](https://img.shields.io/badge/Cost-Free%20Tier-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

A cloud-hosted resume website built on AWS, inspired by the
[Cloud Resume Challenge](https://cloudresumechallenge.dev/).

## 🌐 Live Demo
👉 https://d35mg4ts5diiqf.cloudfront.net

## ✨ Features
- Static resume hosted on Amazon S3
- Global CDN delivery via CloudFront with HTTPS
- Live visitor counter using Lambda + DynamoDB + API Gateway
- Secured with IAM least-privilege roles

## 🛠 AWS Services Used
| Service | Purpose |
|---|---|
| S3 | Hosts the static HTML/CSS resume |
| CloudFront | CDN + HTTPS global delivery |
| Lambda (Python) | Serverless visitor counter |
| DynamoDB | Stores visitor count |
| API Gateway | REST API endpoint |
| IAM | Security and permissions |

## 📁 Project Structure
## 💰 Cost
~$0/month on AWS Free Tier

## 📚 What I Learned
- Hosting static websites on S3 with CloudFront CDN
- Building serverless APIs with Lambda and API Gateway
- NoSQL database operations with DynamoDB
- IAM roles and least-privilege security
- Cloud architecture design

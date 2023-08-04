#!/usr/bin/env python
# coding: utf-8

# In[1]:


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_cover_letter(company_name, company_values, company_vision, company_reputation, company_culture):
    # Read cover letter template from a file
    with open('cover_letter_template.txt', 'r') as file:
        cover_letter_template = file.read()

    cover_letter = cover_letter_template.format(
        company_name=company_name,
        company_values=company_values,
        company_vision=company_vision,
        company_reputation=company_reputation,
        company_culture=company_culture
    )

    return cover_letter

def save_cover_letter_to_pdf(company_name, cover_letter):
    # Create a PDF file with the cover letter content
    pdf_file = f"{company_name} Cover Letter.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    styles = getSampleStyleSheet()

    # Add the paragraphs to the document
    content = []
    for paragraph in cover_letter.split('\n'):
        if paragraph.strip():
            content.append(Paragraph(paragraph.strip(), styles['Normal']))
            content.append(Spacer(1, 12))  # Add some space between paragraphs

    doc.build(content)

def main():
    # Example company name, values, vision, reputation, and culture
    company_name = "DataTech Solutions"
    company_values = "Innovation, Collaboration, Customer Satisfaction"
    company_vision = "Transforming data into actionable insights for a better world."
    company_reputation = "innovative solutions and top-notch data analytics services"
    company_culture = "employee-driven, fostering creativity and open communication"

    cover_letter = generate_cover_letter(
        company_name,
        company_values,
        company_vision,
        company_reputation,
        company_culture
    )

    # Save the cover letter to a PDF file using ReportLab
    save_cover_letter_to_pdf(company_name, cover_letter)

if __name__ == "__main__":
    main()


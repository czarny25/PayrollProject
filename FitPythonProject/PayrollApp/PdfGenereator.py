'''
Created on 6 Jun 2020

@author: czarn

/usr/bin/env python


'''


from __future__ import print_function
from sys import argv

from reportlab.pdfgen import canvas
from _datetime import date

point = 1
inch = 72

TEXT = """%s    page %d of %d
a wonderful file
created with Sample_Code/makesimple.py"""


def make_pdf_file(output_filename, np):
    #title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 6 * inch))
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 12 * point)
    
    '''
    # Add content for payslip 
    for pn in range(1, np + 1):
        v = 10 * inch
        for subtline in (TEXT % (output_filename, pn, np)).split( '\n' ):
            c.drawString( 1 * inch, v, subtline )
            v -= 12 * point
        c.showPage()
    '''   
    c.drawString( TEXT )   
    c.save()
    print()



numOfWeek = 23


make_pdf_file("Payslip Week %d.pdf"%numOfWeek, 1)

print ("Wrote", "Payslip Week %d.pdf"%numOfWeek)


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
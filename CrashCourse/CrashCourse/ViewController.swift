//
//  ViewController.swift
//  CrashCourse
//
//  Created by Zyon Savery on 3/13/21.
//

import UIKit

class ViewController: UIViewController {
    
    
    // Label
    @IBOutlet weak var label1: UILabel!
    
    // Text Field
    @IBOutlet weak var body1: UITextView!
    
    // Button
    @IBOutlet weak var button1: UIButton!
    
    
    
    
    // Don't worry about this for now!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //label1
        // Create string
        var msg : String = "Hello"
        
        //
        // button1
        // Change Button Color to gray
        button1.backgroundColor = UIColor.gray
        // Curve Button Corners
        button1.layer.cornerRadius = 7
        // Change Font Color to White
        button1.setTitleColor(UIColor.white, for: .normal)
        // Change Font Text to "Add text to Label"
        button1.setTitle("Add text to Label", for: .normal)
        
        
        
        
        

    }


}



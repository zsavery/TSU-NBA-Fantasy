//
//  AppDelegate.swift
//  TSU-NBA-FANTASY
//
//  Created by Jachike Uzendu on 3/15/21.
//

import UIKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
     var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        self.window = UIWindow(frame: UIScreen.main.bounds)
        
        // making sure that self.window exist by setting to local variable windowX, if not return false
        guard let windowX = self.window else {
            return false
        }
        let viewController = OutterViewController(frame: windowX.bounds)
        self.window?.rootViewController = viewController
        self.window?.makeKeyAndVisible()
        return true
    }

}

